from uuid import UUID

from typing_extensions import Any, List, NotRequired, TypedDict, Union


class SubredditResponseData(TypedDict):
    """Response data from Reddit API"""

    kind: str
    data: "ListingData"


class ListingData(TypedDict):
    """Class representing the data field of a Listing response"""

    approved_at_utc: NotRequired[None]
    subreddit: NotRequired[str]
    selftext: NotRequired[str]
    author_fullname: NotRequired[str]
    saved: NotRequired[bool]
    mod_reason_title: NotRequired[None]
    gilded: NotRequired[int]
    clicked: NotRequired[bool]
    title: NotRequired[str]
    link_flair_richtext: NotRequired[List["LinkFlairRichtext"]]
    subreddit_name_prefixed: NotRequired[str]
    hidden: NotRequired[bool]
    pwls: NotRequired[int]
    link_flair_css_class: NotRequired[str]
    downs: NotRequired[int]
    thumbnail_height: NotRequired[Union[None, int]]
    top_awarded_type: NotRequired[None]
    hide_score: NotRequired[bool]
    name: NotRequired[str]
    quarantine: NotRequired[bool]
    link_flair_text_color: NotRequired[str]
    upvote_ratio: NotRequired[float]
    author_flair_background_color: NotRequired[None]
    subreddit_type: NotRequired[str]
    ups: NotRequired[int]
    total_awards_received: NotRequired[int]
    media_embed: NotRequired[Any]
    thumbnail_width: NotRequired[Union[None, int]]
    author_flair_template_id: NotRequired[None]
    is_original_content: NotRequired[bool]
    user_reports: NotRequired[List[Any]]
    secure_media: NotRequired[None]
    is_reddit_media_domain: NotRequired[bool]
    is_meta: NotRequired[bool]
    category: NotRequired[None]
    secure_media_embed: NotRequired[Any]
    link_flair_text: NotRequired[str]
    can_mod_post: NotRequired[bool]
    score: NotRequired[int]
    approved_by: NotRequired[None]
    is_created_from_ads_ui: NotRequired[bool]
    author_premium: NotRequired[bool]
    thumbnail: NotRequired[str]
    edited: NotRequired[bool]
    author_flair_css_class: NotRequired[None]
    author_flair_richtext: NotRequired[List[Any]]
    gildings: NotRequired[Any]
    content_categories: NotRequired[None]
    is_self: NotRequired[bool]
    mod_note: NotRequired[None]
    created: NotRequired[float]
    link_flair_type: NotRequired[str]
    wls: NotRequired[int]
    removed_by_category: NotRequired[None]
    banned_by: NotRequired[None]
    author_flair_type: NotRequired[str]
    domain: NotRequired[str]
    allow_live_comments: NotRequired[bool]
    selftext_html: NotRequired[Union[None, str]]
    likes: NotRequired[None]
    suggested_sort: NotRequired[str]
    banned_at_utc: NotRequired[None]
    view_count: NotRequired[None]
    archived: NotRequired[bool]
    no_follow: NotRequired[bool]
    is_crosspostable: NotRequired[bool]
    pinned: NotRequired[bool]
    over_18: NotRequired[bool]
    all_awardings: NotRequired[List[Any]]
    awarders: NotRequired[List[Any]]
    media_only: NotRequired[bool]
    link_flair_template_id: NotRequired[UUID]
    can_gild: NotRequired[bool]
    spoiler: NotRequired[bool]
    locked: NotRequired[bool]
    author_flair_text: NotRequired[None]
    treatment_tags: NotRequired[List[Any]]
    visited: NotRequired[bool]
    removed_by: NotRequired[None]
    num_reports: NotRequired[None]
    distinguished: NotRequired[None]
    subreddit_id: NotRequired[str]
    author_is_blocked: NotRequired[bool]
    mod_reason_by: NotRequired[None]
    removal_reason: NotRequired[None]
    link_flair_background_color: NotRequired[str]
    id: NotRequired[str]
    is_robot_indexable: NotRequired[bool]
    report_reasons: NotRequired[None]
    author: NotRequired[str]
    discussion_type: NotRequired[None]
    num_comments: NotRequired[int]
    send_replies: NotRequired[bool]
    whitelist_status: NotRequired[str]
    contest_mode: NotRequired[bool]
    mod_reports: NotRequired[List[Any]]
    author_patreon_flair: NotRequired[bool]
    author_flair_text_color: NotRequired[None]
    permalink: NotRequired[str]
    parent_whitelist_status: NotRequired[str]
    stickied: NotRequired[bool]
    url: NotRequired[str]
    subreddit_subscribers: NotRequired[int]
    created_utc: NotRequired[float]
    num_crossposts: NotRequired[int]
    media: NotRequired[None]
    is_video: NotRequired[bool]
    post_hint: NotRequired[str]
    url_overridden_by_dest: NotRequired[str]
    preview: NotRequired["Preview"]
    after: NotRequired[str]
    dist: NotRequired[int]
    modhash: NotRequired[str]
    geo_filter: NotRequired[str]
    children: NotRequired[List[SubredditResponseData]]
    before: NotRequired[None]


class LinkFlairRichtext(TypedDict):
    """Class representing the link_flair_richtext field of a Listing response"""

    e: str
    t: NotRequired[str]
    a: NotRequired[str]
    u: NotRequired[str]


class Image(TypedDict):
    """Class representing the images field of a post"""

    source: "SourceOrResolution"
    resolutions: List["SourceOrResolution"]
    variants: Any
    id: str


class Preview(TypedDict):
    """Class representing the preview field of a post"""

    images: List[Image]
    enabled: bool


class SourceOrResolution(TypedDict):
    """Class representing the source or resolutions field of a post"""

    url: str
    width: int
    height: int
