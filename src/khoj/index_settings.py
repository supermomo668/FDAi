from django.http import Http404
from asgiref.sync import sync_to_async
from typing import Optional

from khoj.database.models import KhojUser
import os

class KhojUserNotFound(Exception):
    pass
  

async def getStaffUser(
    username: str = os.getenv("ENTRYSTORE_ADMIN_USERNAME")) -> Optional[KhojUser]:
    user_query = await sync_to_async(
        KhojUser.objects.filter(is_staff=True, username=username).first
    )()
    if not user_query:
        # Here you can choose to raise Http404 if you're using this within Django views
        # or raise a custom exception if it's a standalone async application.
        raise KhojUserNotFound(f"Staff user with username {username} not found.")
    return user_query


from khoj.utils.state import SearchType
# Fix based on search types

async def get_entry_admin_users():
    return {
    SearchType.Org.value: False,
    SearchType.Markdown.value: False,
    SearchType.Plaintext.value: False,
    SearchType.Pdf.value: False,
    SearchType.Github.value: await getStaffUser(
        os.getenv("GITHUB_ENTRY_ADMIN")
        ) if os.getenv("GITHUB_ENTRY_ADMIN") else False,
    SearchType.Notion.value: False,
    SearchType.All.value: False,
}
