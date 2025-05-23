"""empty message

Revision ID: 588e0e2fc2df
Revises: 77c890b48e1a
Create Date: 2025-03-21 01:47:33.940484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '588e0e2fc2df'
down_revision = '77c890b48e1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.String(length=20), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_gender'), ['gender'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_gender'))
        batch_op.drop_column('gender')

    # ### end Alembic commands ###
