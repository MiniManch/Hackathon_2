"""empty message

Revision ID: cc3b4c517c6f
Revises: 
Create Date: 2023-04-04 15:35:28.533043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc3b4c517c6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_front', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('image_back', sa.String(length=200), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.drop_column('image_back')
        batch_op.drop_column('image_front')

    # ### end Alembic commands ###