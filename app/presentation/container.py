from dependency_injector import containers, providers
from app.application.services.posts_service import IPostsService, PostsService
from app.infrastructure.repository.posts_repository import IPostsRepository, PostsRepository
from app.presentation.config import Config

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            # "app.api.v1.endpoints.auth",
            "app.presentation.routes.v1.posts",
            # "app.api.v1.endpoints.tag",
            # "app.api.v1.endpoints.user",
            # "app.api.v2.endpoints.auth",
            # "app.core.dependencies",
        ]
    )

    configuration : Config = providers.Singleton(Config)
    post_repository : IPostsRepository = providers.Factory(PostsRepository, configuration=configuration)
    post_service : IPostsService = providers.Factory(PostsService, respository=post_repository)

    