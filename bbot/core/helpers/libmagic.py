import puremagic


def get_magic_info(file):

    magic_detections = puremagic.magic_file(file)
    if magic_detections:
        magic_detections.sort(key=lambda x: x.confidence, reverse=True)
        detection = magic_detections[0]
        return detection.extension, detection.mime_type, detection.name, detection.confidence
    return "", "", "", 0


def get_compression(mime_type):
    mime_type = mime_type.lower()
    # from https://github.com/cdgriffith/puremagic/blob/master/puremagic/magic_data.json
    compression_map = {
        "application/gzip": "gzip",  # Gzip compressed file
        "application/zip": "zip",  # Zip archive
        "application/x-bzip2": "bzip2",  # Bzip2 compressed file
        "application/x-xz": "xz",  # XZ compressed file
        "application/x-7z-compressed": "7z",  # 7-Zip archive
        "application/vnd.rar": "rar",  # RAR archive
        "application/x-lzma": "lzma",  # LZMA compressed file
        "application/x-compress": "compress",  # Unix compress file
        "application/zstd": "zstd",  # Zstandard compressed file
        "application/x-lz4": "lz4",  # LZ4 compressed file
        "application/x-tar": "tar",  # Tar archive
        "application/x-zip-compressed-fb2": "zip",  # Zip archive (FB2)
        "application/epub+zip": "zip",  # EPUB book (Zip archive)
        "application/pak": "pak",  # PAK archive
        "application/x-lha": "lha",  # LHA archive
        "application/arj": "arj",  # ARJ archive
        "application/vnd.ms-cab-compressed": "cab",  # Microsoft Cabinet archive
        "application/x-sit": "sit",  # StuffIt archive
        "application/binhex": "binhex",  # BinHex encoded file
        "application/x-lrzip": "lrzip",  # Long Range ZIP
        "application/x-alz": "alz",  # ALZip archive
        "application/x-tgz": "tgz",  # Gzip compressed Tar archive
        "application/x-gzip": "gzip",  # Gzip compressed file
        "application/x-lzip": "lzip",  # Lzip compressed file
        "application/x-zstd-compressed-tar": "zstd",  # Zstandard compressed Tar archive
        "application/x-lz4-compressed-tar": "lz4",  # LZ4 compressed Tar archive
        "application/vnd.comicbook+zip": "zip",  # Comic book archive (Zip)
        "application/vnd.palm": "palm",  # Palm OS data
        "application/fictionbook2+zip": "zip",  # FictionBook 2.0 (Zip)
        "application/fictionbook3+zip": "zip",  # FictionBook 3.0 (Zip)
        "application/x-cpio": "cpio",  # CPIO archive
        "application/x-java-pack200": "pack200",  # Java Pack200 archive
        "application/x-par2": "par2",  # PAR2 recovery file
        "application/x-rar-compressed": "rar",  # RAR archive
        "application/java-archive": "zip",  # Java Archive (JAR)
        "application/x-webarchive": "zip",  # Web archive (Zip)
        "application/vnd.android.package-archive": "zip",  # Android package (APK)
        "application/x-itunes-ipa": "zip",  # iOS application archive (IPA)
        "application/x-stuffit": "sit",  # StuffIt archive
        "application/x-archive": "ar",  # Unix archive
        "application/x-qpress": "qpress",  # Qpress archive
        "application/x-xar": "xar",  # XAR archive
        "application/x-ace": "ace",  # ACE archive
        "application/x-zoo": "zoo",  # Zoo archive
        "application/x-arc": "arc",  # ARC archive
        "application/x-zstd-compressed-tar": "zstd",  # Zstandard compressed Tar archive
        "application/x-lz4-compressed-tar": "lz4",  # LZ4 compressed Tar archive
        "application/vnd.comicbook-rar": "rar",  # Comic book archive (RAR)
    }

    return compression_map.get(mime_type, "")
