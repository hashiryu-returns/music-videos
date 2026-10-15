import AppKit
// sheet.swift <out> <cols> <imgs...>  (each tile 256x144, label = file name)
let a = CommandLine.arguments
let cols = Int(a[2])!
let files = Array(a[3...])
let tw = 256.0, th = 144.0
let rows = (files.count + cols - 1) / cols
let out = NSImage(size: NSSize(width: tw * Double(cols), height: th * Double(rows)))
out.lockFocus()
NSColor.black.setFill(); NSRect(x: 0, y: 0, width: tw * Double(cols), height: th * Double(rows)).fill()
for (i, f) in files.enumerated() {
  guard let img = NSImage(contentsOfFile: f) else { continue }
  let c = i % cols, r = i / cols
  let rect = NSRect(x: Double(c) * tw, y: Double(rows - 1 - r) * th, width: tw, height: th)
  img.draw(in: rect)
  let name = (f as NSString).lastPathComponent.replacingOccurrences(of: ".jpg", with: "")
  let attrs: [NSAttributedString.Key: Any] = [.font: NSFont.boldSystemFont(ofSize: 11), .foregroundColor: NSColor.yellow, .backgroundColor: NSColor.black.withAlphaComponent(0.6)]
  (name as NSString).draw(at: NSPoint(x: rect.minX + 3, y: rect.minY + 3), withAttributes: attrs)
}
out.unlockFocus()
let rep = NSBitmapImageRep(data: out.tiffRepresentation!)!
try! rep.representation(using: .jpeg, properties: [.compressionFactor: 0.85])!.write(to: URL(fileURLWithPath: a[1]))
