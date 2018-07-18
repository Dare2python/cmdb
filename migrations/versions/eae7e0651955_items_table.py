"""items table

Revision ID: eae7e0651955
Revises: 22ecfb52c840
Create Date: 2018-07-18 18:29:40.410639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eae7e0651955'
down_revision = '22ecfb52c840'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_name'), 'item', ['name'], unique=False)
    op.create_index(op.f('ix_item_timestamp'), 'item', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_timestamp'), table_name='item')
    op.drop_index(op.f('ix_item_name'), table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###
