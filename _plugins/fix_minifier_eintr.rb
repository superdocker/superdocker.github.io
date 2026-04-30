module Jekyll
  module Compressor
    def output_file(dest, content)
      FileUtils.mkdir_p(File.dirname(dest))
      begin
        File.open(dest, 'w') { |f| f.write(content) }
      rescue Errno::EINTR
        retry
      end
    end
  end

  class StaticFile
    def copy_file(path, dest_path)
      FileUtils.mkdir_p(File.dirname(dest_path))
      begin
        FileUtils.cp(path, dest_path)
      rescue Errno::EINTR
        retry
      end
    end
  end
end
