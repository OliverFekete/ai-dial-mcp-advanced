from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool

class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "search_users"

    @property
    def description(self) -> str:
        return "Searches for users by name, surname, email, or gender. All parameters are optional."

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "User's first name"},
                "surname": {"type": "string", "description": "User's surname"},
                "email": {"type": "string", "description": "User's email"},
                "gender": {"type": "string", "description": "User's gender"}
            },
            "required": []
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        return await self._user_client.search_users(**arguments)