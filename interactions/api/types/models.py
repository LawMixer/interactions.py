import datetime
from typing import Optional, Union, List


# TODO: Reorganise these models based on which big obj uses little obj
# TODO: Figure out ? placements.

# 'Optional[datetime.datetime]` is the Timestamp, just a mini note
from interactions.api.types.enums import GuildFeature


class MessageActivity(object):
    type: int
    party_id: Optional[str]


class MessageReference(object):
    message_id: Optional[int]
    channel_id: Optional[int]
    guild_id: Optional[int]
    fail_if_not_exists: Optional[bool]


class ThreadMetadata(object):
    archived: bool
    auto_archive_duration: int
    archive_timestamp: datetime.datetime.timestamp
    locked: bool
    invitable: Optional[bool]


class ThreadMember(object):
    id: Optional[int]  # intents
    user_id: Optional[int]
    join_timestamp: datetime.datetime.timestamp
    flags: int


class User(object):
    id: int
    username: str
    discriminator: str
    avatar: Optional[str]
    bot: Optional[bool]
    system: Optional[bool]
    mfa_enabled: Optional[bool]
    banner: Optional[str]
    accent_color: Optional[int]
    locale: Optional[str]
    verified: Optional[bool]
    email: Optional[str]
    flags: int
    premium_type: int
    public_flags: int

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Member(object):
    """Also, the guild member obj (Or partial.)"""

    user: Optional[User]
    nick: Optional[str]
    roles: List[str]
    joined_at: datetime.datetime.timestamp
    premium_since: Optional[datetime.datetime]
    deaf: bool
    mute: bool
    pending: Optional[bool]
    permissions: Optional[str]


class Overwrite(object):
    """This is used for the PermissionOverride obj"""

    id: int
    type: int
    allow: str
    deny: str


class Channel(object):
    """
    The big Channel model.

    The purpose of this model is to be used as a base class, and
    is never needed to be used directly.
    """

    id: int  # "Snowflake"
    type: int
    guild_id: Optional[int]
    position: Optional[int]
    permission_overwrites: List[Overwrite]
    name: str  # This apparently exists in DMs. Untested in v9, known in v6
    topic: Optional[str]
    nsfw: Optional[bool]
    last_message_id: Optional[int]
    bitrate: Optional[int]  # not really needed in our case
    user_limit: Optional[int]
    rate_limit_per_user: Optional[int]
    recipients: Optional[List[User]]
    icon: Optional[str]
    owner_id: Optional[int]
    application_id: Optional[int]
    parent_id: Optional[int]
    last_pin_timestamp: Optional[datetime.datetime]
    rtc_region: Optional[str]
    video_quality_mode: Optional[int]
    message_count: Optional[int]
    member_count: Optional[int]
    thread_metadata: Optional[ThreadMetadata]
    member: Optional[ThreadMember]
    default_auto_archive_duration: Optional[int]
    permissions: Optional[str]

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Attachment(object):
    id: int
    filename: str
    content_type: Optional[str]
    size: int
    url: str
    proxy_url: str
    height: Optional[int]
    width: Optional[int]


class Message(object):
    """
    The big Message model.

    The purpose of this model is to be used as a base class, and
    is never needed to be used directly.
    """
    id: int
    channel_id: int
    guild_id: Optional[int]
    author: User
    member: Optional[Member]
    content: str
    timestamp: datetime.datetime.timestamp
    edited_timestamp: Optional[datetime.datetime]
    tts: bool
    mention_everyone: bool
    # mentions: array of Users, and maybe partial members
    mentions = Optional[List[Union[Member, User]]]
    mention_roles: Optional[List[str]]
    mention_channels: Optional[List["ChannelMention"]]
    attachments: Optional[List[Attachment]]
    # embeds
    reactions: Optional[List["ReactionObject"]]
    nonce: Union[int, str]
    pinned: bool
    webhook_id: Optional[int]
    type: int
    activity: Optional[MessageActivity]
    # application
    application_id: int
    message_reference: Optional[MessageReference]
    flags: int
    referenced_message: Optional["Message"]  # pycharm says it works, idk
    # interaction
    thread: Optional[Channel]

    # components
    # s sticker items
    # stickers

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Emoji(object):
    id: Optional[int]
    name: Optional[str]
    roles: Optional[List[str]]
    user: Optional[User]
    require_colons: Optional[bool]
    managed: Optional[bool]
    animated: Optional[bool]
    available: Optional[bool]

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ReactionObject(object):
    count: int
    me: bool
    emoji: Emoji


class RoleTags(object):
    bot_id: Optional[int]
    integration_id: Optional[int]
    premium_subscriber: Optional[int]

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Role(object):
    id: int
    name: str
    color: int
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: Optional[RoleTags]

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ChannelMention(object):
    id: int
    guild_id: int
    type: int  # Replace with enum from Channel Type, another PR
    name: str

class PresenceActivity(object):
    name: str
    type: int
    url: Optional[str]
    created_at: int
    timestamps: Optional[datetime.datetime]
    application_id: Optional[int]
    details: Optional[str]
    state: Optional[str]
    emoji: Optional[Emoji]
    # party
    #assets
    # secrets
    instance: Optional[bool]
    flags: Optional[int]
    # buttons

class ClientStatus(object):
    desktop: Optional[str]
    mobile: Optional[str]
    web: Optional[str]

class PresenceUpdate(object):
    user: User
    guild_id: int
    status: str
    activities: List[PresenceActivity]
    client_status: ClientStatus


class Guild(object):
    """The big Guild object."""

    id: int
    name: str
    icon: Optional[str]
    icon_hash: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: Optional[bool]
    owner_id: int
    permissions: Optional[str]
    region: Optional[str]  # None, we don't do Voices.
    afk_channel_id: Optional[int]
    afk_timeout: int
    widget_enabled: Optional[bool]
    widget_channel_id: Optional[int]
    verification_level: int
    default_message_notifications: int
    explicit_content_filter: int
    roles: List[Role]
    emojis: List[Emoji]
    features: List[GuildFeature]
    mfa_level: int
    application_id: Optional[int]
    system_channel_id: Optional[int]
    system_channel_flags: int
    rules_channel_id: Optional[int]
    joined_at: Optional[datetime.datetime]
    large: Optional[bool]
    unavailable: Optional[bool]
    member_count: Optional[int]
    # Voice states. They're None due to v4.0 property
    members: Optional[List[Member]]
    channels: Optional[List[Channel]]
    threads: Optional[List[Channel]]  # threads, because of their metadata
    # presences: Optional[List[]]
    max_presences: Optional[int]
    max_members: Optional[int]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: int
    premium_subscription_count: Optional[int]
    preferred_locale: str
    public_updates_channel_id: Optional[int]
    max_video_channel_users: Optional[int]
    approximate_member_count: Optional[int]
    approximate_presence_count: Optional[int]
    # welcome_Screen
    nsfw_level: int
    # stage_instances
    # stickers
