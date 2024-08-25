from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import VideoFileClip

def split_video(mp4_file, timestamp_file):
    with open(timestamp_file, 'r') as file:
        for line in file:
            start_time, end_time, new_video_name = line.strip().split(',')
            start_time = time_to_seconds(start_time)
            end_time = time_to_seconds(end_time)

            ffmpeg_extract_subclip(mp4_file, start_time, end_time, targetname=new_video_name)

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# Example usage
mp4_file = r"vod.mp4" # name of downloaded video with file extension

timestamp_file = 'timestamps.txt'
split_video(mp4_file, timestamp_file)

# timestamp format for timestamps.txt
# hh:mm:ss, hh:mm:ss, P1_name (P1_char) vs P2_name (P2_char) - Tourney_name - Tourney_round.mp4
# use commas to include multiple chars for 1 player