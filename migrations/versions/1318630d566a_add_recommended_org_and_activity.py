"""add recommended org and activity

Revision ID: 1318630d566a
Revises: 55b4619add57
Create Date: 2014-11-13 20:32:41.323748

"""

# revision identifiers, used by Alembic.
revision = '1318630d566a'
down_revision = '55b4619add57'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recommended_activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('created', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recommended_org',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('created', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recommended_org')
    op.drop_table('recommended_activity')
    ### end Alembic commands ###
