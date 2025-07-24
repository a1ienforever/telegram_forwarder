from app.interfaces.storage.models import Channel
from app.interfaces.storage.repos.base_repo import BaseRepo


class ChannelRepo(BaseRepo):
    model = Channel
