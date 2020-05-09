"""empty message

Revision ID: 0cfbb70ce235
Revises: 925b93d92809
Create Date: 2020-05-07 22:40:06.773148

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cfbb70ce235'
down_revision = '925b93d92809'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('deleted_alias_user_id_fkey', 'deleted_alias', type_='foreignkey')
    op.drop_column('deleted_alias', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deleted_alias', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('deleted_alias_user_id_fkey', 'deleted_alias', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
