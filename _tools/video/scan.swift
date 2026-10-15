import AVFoundation
import CoreImage
// scan.swift <clip> [start] [end] : every frame -> "idx time bright diff sat"
let a = CommandLine.arguments
let asset = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let track = asset.tracks(withMediaType: .video)[0]
let fps = Double(track.nominalFrameRate)
let r = try! AVAssetReader(asset: asset)
let start = a.count > 2 ? Double(a[2])! : 0
let end = a.count > 3 ? Double(a[3])! : CMTimeGetSeconds(asset.duration)
r.timeRange = CMTimeRange(start: CMTime(seconds: start, preferredTimescale: 600), end: CMTime(seconds: end, preferredTimescale: 600))
let out = AVAssetReaderTrackOutput(track: track, outputSettings: [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA])
r.add(out); r.startReading()
var prev: [Float]? = nil
print("fps \(fps)")
while let sb = out.copyNextSampleBuffer() {
  guard let pb = CMSampleBufferGetImageBuffer(sb) else { continue }
  let t = CMTimeGetSeconds(CMSampleBufferGetPresentationTimeStamp(sb))
  CVPixelBufferLockBaseAddress(pb, .readOnly)
  let w = CVPixelBufferGetWidth(pb), h = CVPixelBufferGetHeight(pb), bpr = CVPixelBufferGetBytesPerRow(pb)
  let base = CVPixelBufferGetBaseAddress(pb)!.assumingMemoryBound(to: UInt8.self)
  let gx = 32, gy = 18
  var cur = [Float](repeating: 0, count: gx * gy)
  var sum: Float = 0, sat: Float = 0
  for j in 0..<gy { for i in 0..<gx {
    let x = i * w / gx + w / gx / 2, y = j * h / gy + h / gy / 2
    let p = base + y * bpr + x * 4
    let b = Float(p[0]) / 255, g = Float(p[1]) / 255, rr = Float(p[2]) / 255
    let l = 0.299 * rr + 0.587 * g + 0.114 * b
    cur[j * gx + i] = l; sum += l
    sat += max(rr, g, b) - min(rr, g, b)
  } }
  CVPixelBufferUnlockBaseAddress(pb, .readOnly)
  var d: Float = 0
  if let p = prev { for k in 0..<cur.count { d += abs(cur[k] - p[k]) }; d /= Float(cur.count) }
  prev = cur
  let n = cur.count
  print(String(format: "%5d %7.3f bright %.3f diff %.4f sat %.3f", Int((t * fps).rounded()), t, sum / Float(n), d, sat / Float(n)))
}
