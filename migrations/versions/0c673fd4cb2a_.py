"""empty message

Revision ID: 0c673fd4cb2a
Revises: 
Create Date: 2022-03-27 12:35:02.033007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c673fd4cb2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('despesas')
    op.drop_table('receitas')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('receitas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('descricao', sa.VARCHAR(length=2000), nullable=True),
    sa.Column('valor', sa.FLOAT(), nullable=True),
    sa.Column('data', sa.VARCHAR(length=11), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('despesas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('descricao', sa.VARCHAR(length=2000), nullable=True),
    sa.Column('valor', sa.FLOAT(), nullable=True),
    sa.Column('data', sa.VARCHAR(length=85), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###