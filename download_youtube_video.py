from os import makedirs
from pytube import YouTube


def download_youtube_video(url, audio_only=False, output_path=None, filename=None, filename_prefix=None):
    """
    Download a YouTube Video.
    :param url: Full URL to YouTube Video or YouTube Video ID
    :type url: str
    :param audio_only: Download only the audio for the video. Takes longer than video.
    :type audio_only: bool
    :param output_path: Path to folder to output file.
    :type output_path: str
    :param filename: Filename override. Does not override extension.
    :type filename: str
    :param filename_prefix: Currently Does Not Work on pytube
    :type filename_prefix: str
    :return: Filename of downloaded video/audio
    :rtype: str
    """
    if output_path:
        makedirs(output_path, exist_ok=True)
    if 'https' not in url:
        url = 'https://www.youtube.com/watch?v=%s' % url
    video = YouTube(url)
    if audio_only:
        stream = video.streams.filter(only_audio=True).first()
    else:
        stream = video.streams.first()
    print('Download Started: %s' % video.title)
    stream.download(output_path=output_path, filename=filename)
    print('Download Complete: %s' % video.title)
    return video.title + '.mp4' if filename is None else filename + '.mp4'