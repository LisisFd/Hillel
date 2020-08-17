import asyncio
import aiohttp
import json


async def request_data(url):
    async with aiohttp.request('GET', f'https://www.reddit.com/r/{url}/hot.json?sort=top&t=day&limit=5') \
            as context:
        dict_json = await context.json()
        return dict_json


async def get_reddit_top(subreddit):
    """
    :param subreddit: Section title
    :return: parse_dict - dict sorted about value, string_dict - dict in sting format, if you need print
    """
    data_json = await request_data(subreddit)
    parse_dict = {
        subreddit: list()
    }
    post_score = 0
    for elem in data_json.get('data').get('children'):
        post_title = elem.get('data').get('title')  
        post_link = elem.get('data').get('url')
        post_score += 1
        parse_dict.get(subreddit).append(
            {post_title: {
                'score': post_score,
                'link': post_link
            }}
        )
    string_dict = json.dumps(parse_dict, indent=4, sort_keys=True)
    return parse_dict, string_dict


async def main():
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    res = await asyncio.gather(*(get_reddit_top(subreddit) for subreddit in reddits))

asyncio.run(main())
