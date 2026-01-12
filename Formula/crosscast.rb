class Crosscast < Formula
  desc "Cross-platform file sharing tool (AirDrop alternative)"
  homepage "https://github.com/thelonewolf39/homebrew-CrossCast"
  url "https://github.com/thelonewolf39/homebrew-CrossCast/archive/refs/heads/main.zip"
  version "0.1.0"
  depends_on "python@3.11"

  def install
    bin.install "crosscast/crosscast.py" => "crosscast"
  end

  test do
    system "#{bin}/crosscast", "--help"
  end
end
