"""
Added Youtube channel to Newsboat URLs:
    youtube channel url: https://www.youtube.com/channel/UCUZHFZ9jIKrLroW8LcyJEQQ
    newsboat url: https://www.youtube.com/feeds/videos.xml?channel_id=UCUZHFZ9jIKrLroW8LcyJEQQ
"""
import config
import re

CHANNEL_URL = config.DEFAULT_CONFIG["CHANNEL_URL"]
NEWSBOAT_URLS_FILE = config.DEFAULT_CONFIG["NEWSBOAT_URLS_FILE"]


def validate_channel_id(channel_id) -> None:
    """ Validate Channel ID by regexp """
    string = channel_id
    pattern = re.compile("[0-9A-Za-z_-]{21}[AQgw]")
    match = pattern.search(string)
    if not match:
        print(f"Channel Id {string} is not valid. Exit.")
        exit()


def get_channel_id() -> str:
    """ Return channel id from Youtube channel URL."""
    channel_id = CHANNEL_URL.split("/")[4]
    validate_channel_id(channel_id)
    return channel_id


def create_rss_link() -> str:
    """ Generate Newsboat compatible RSS link. """
    template_url = "https://www.youtube.com/feeds/videos.xml?channel_id="
    channel_id = get_channel_id()
    return template_url + channel_id


def check_already_exists(newsboat_url) -> None:
    """ Exit if channel id already exists in newsboat urls. """
    with open(NEWSBOAT_URLS_FILE, "r") as file:
        for line in file:
            if newsboat_url in line:
                print("YouTube Channel already exist in Newboat URLs. Nothing to do.")
                exit()
    print(f"[Adding] {newsboat_url} to Newsboat list..")


def get_count_newsboat_urls() -> int:
    """ Return number of lines from URLs file. """
    num_lines = sum(1 for line in open(NEWSBOAT_URLS_FILE))
    return num_lines


def add_newsboat_url(newsboat_url) -> None:
    """ Add correct newsboat url with Youtube channel. """
    check_already_exists(newsboat_url)
    with open(NEWSBOAT_URLS_FILE, "a") as file:
        data = newsboat_url
        file.write(data + '\n')
    count = get_count_newsboat_urls()
    print(f"[Added] URL to Newsboat list. Now {count} URLs in file.")


if __name__ == "__main__":
    newsboat_url = create_rss_link()
    print(f"[URL] {newsboat_url}")
    add_newsboat_url(newsboat_url)
