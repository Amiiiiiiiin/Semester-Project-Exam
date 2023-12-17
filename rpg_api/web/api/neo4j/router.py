from fastapi import APIRouter

from rpg_api.web.api.neo4j import auth, users, relation


neo4j_router = APIRouter()


neo4j_router.include_router(auth.router, prefix="/auth")
neo4j_router.include_router(users.router, prefix="/users")
neo4j_router.include_router(relation.router, prefix="/relation")