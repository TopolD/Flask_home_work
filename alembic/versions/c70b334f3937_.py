"""empty message

Revision ID: c70b334f3937
Revises: 84e0afbb5b29
Create Date: 2023-11-04 10:44:24.492312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c70b334f3937'
down_revision: Union[str, None] = '84e0afbb5b29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('Dish_name', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'order_dishes', ['Dish_name'], ['ID_DISH'])
    op.drop_column('orders', 'DISH')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('DISH', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'order_dishes', ['DISH'], ['ID_DISH'])
    op.drop_column('orders', 'Dish_name')
    # ### end Alembic commands ###
