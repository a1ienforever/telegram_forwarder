from app.adapters.database.models import Channel
from app.adapters.database.repositories.base_repo import BaseRepo


class ChannelRepo(BaseRepo):
    model = Channel
