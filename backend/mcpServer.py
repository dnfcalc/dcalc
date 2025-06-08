
from fastmcp import FastMCP
from main import application
from fastmcp.server.openapi import RouteMap, MCPType, HTTPRoute


def custom_route_mapper(route: HTTPRoute, mcp_type: MCPType) -> MCPType | None:
    """Advanced route type mapping."""
    # Convert all admin routes to tools regardless of HTTP method
    if "/open/" in route.path and route.method in ["GET"]:
        return MCPType.TOOL
    else:
        return MCPType.EXCLUDE

mcp = FastMCP.from_fastapi(
    app=application,
    name="My Custom Server",
    timeout=5.0, # Custom component names
    port=1486,
    route_map_fn=custom_route_mapper,
)

mcp.run(transport="streamable-http")
