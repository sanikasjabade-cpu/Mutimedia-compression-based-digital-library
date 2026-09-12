import os
import zipfile

def compress_file(input_path, output_folder):
    """
    Compress any file (audio/image/video/pdf) into zip
    and return original and compressed sizes.
    """
    try:
        os.makedirs(output_folder, exist_ok=True)

        filename = os.path.basename(input_path)
        name, _ = os.path.splitext(filename)

        compressed_path = os.path.join(output_folder, name + ".zip")

        # 🔥 ZIP COMPRESSION
        with zipfile.ZipFile(compressed_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(input_path, filename)

        # size calculation
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(compressed_path)

        return original_size, compressed_size, compressed_path

    except Exception as e:
        print("Compression error:", e)
        return None, None, None
