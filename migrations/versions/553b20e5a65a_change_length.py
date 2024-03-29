"""change length

Revision ID: 553b20e5a65a
Revises: 44a44f522dc
Create Date: 2014-11-11 12:12:49.824164

"""

# revision identifiers, used by Alembic.
revision = '553b20e5a65a'
down_revision = '44a44f522dc'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('organizations', 'authorization',
               existing_type=mysql.CHAR(length=36),
               type_=sa.String(length=255),
               existing_nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('organizations', 'authorization',
               existing_type=sa.String(length=255),
               type_=mysql.CHAR(length=36),
               existing_nullable=False)
    ### end Alembic commands ###
