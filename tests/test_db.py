from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    # Usamos mock_db_time diretamente como o valor esperado
    new_user = User(
        username='alice',
        password='secret',
        email='teste@test',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.id == 1
    assert user.username == 'alice'
    assert user.email == 'teste@test'
    assert user.password == 'secret'
    assert user.created_at is not None
    assert user.updated_at is not None
