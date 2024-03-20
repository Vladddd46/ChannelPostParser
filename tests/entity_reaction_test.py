import pytest
from src.entities.Reaction import Reaction, ReactionType


@pytest.fixture
def sample_reaction():
    return Reaction(5, "😊", False, 1)

def test_reaction_equality(sample_reaction):
    reaction1 = sample_reaction
    reaction2 = Reaction(5, "😊", False, 1)
    assert reaction1 == reaction2
    assert hash(reaction1) == hash(reaction2)

