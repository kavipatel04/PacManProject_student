#TEST to push
import pytest
import pygame


@pytest.fixture(autouse=True)
def pygame_setup():
    pygame.init()
    pygame.display.set_mode((800, 600))
    yield
    pygame.quit()
