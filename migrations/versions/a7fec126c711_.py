"""empty message

Revision ID: a7fec126c711
Revises: 
Create Date: 2023-04-20 07:04:58.595090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7fec126c711'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blocklists', schema=None) as batch_op:
        batch_op.add_column(sa.Column('jti', sa.String(), nullable=False))
        batch_op.drop_column('token')

    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    with op.batch_alter_table('blocklists', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.drop_column('jti')

    # ### end Alembic commands ###
