import AVFoundation
import AppKit
// grab.swift <clip> <prefix> <maxsize> <secs...>
let a = CommandLine.arguments
let asset = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let g = AVAssetImageGenerator(asset: asset)
g.appliesPreferredTrackTransform = true
let m = Double(a[3])!
g.maximumSize = CGSize(width: m, height: m)
g.requestedTimeToleranceBefore = .zero; g.requestedTimeToleranceAfter = .zero
for s in a[4...] {
  let t = CMTime(seconds: Double(s)!, preferredTimescale: 600)
  if let img = try? g.copyCGImage(at: t, actualTime: nil) {
    let rep = NSBitmapImageRep(cgImage: img)
    try! rep.representation(using: .jpeg, properties: [:])!.write(to: URL(fileURLWithPath: "\(a[2])_\(s).jpg"))
  }
}
