"""update

Revision ID: 31886214ea07
Revises: 3c13f01fa0fa
Create Date: 2014-10-19 00:48:14.131158

"""

# revision identifiers, used by Alembic.
revision = '31886214ea07'
down_revision = '3c13f01fa0fa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Unicode(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('class_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('time_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classes_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Unicode(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.Unicode(length=12), nullable=True),
    sa.Column('district', sa.Unicode(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity_orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Date(), nullable=True),
    sa.Column('name', sa.Unicode(length=24), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.Column('cellphone', sa.CHAR(length=11), nullable=True),
    sa.Column('address', sa.Unicode(length=128), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('remark', sa.Unicode(length=100), nullable=True),
    sa.Column('canceled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cellphone', sa.CHAR(length=11), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('member_since', sa.TIMESTAMP(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('contact', sa.Unicode(length=16), nullable=True),
    sa.Column('address', sa.Unicode(length=256), nullable=True),
    sa.Column('authorization', sa.CHAR(length=32), nullable=True),
    sa.Column('photo', sa.CHAR(length=32), nullable=True),
    sa.Column('profession', sa.Integer(), nullable=True),
    sa.Column('property', sa.Integer(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('location', sa.Integer(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('intro', sa.UnicodeText(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('page_view', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Unicode(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Unicode(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('class_orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Date(), nullable=True),
    sa.Column('name', sa.Unicode(length=24), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.Column('cellphone', sa.CHAR(length=11), nullable=True),
    sa.Column('address', sa.Unicode(length=128), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('remark', sa.Unicode(length=100), nullable=True),
    sa.Column('canceled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Unicode(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('age_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('end_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('intro', sa.UnicodeText(), nullable=True),
    sa.Column('closed', sa.Boolean(), nullable=True),
    sa.Column('page_view', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('site_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cellphone', sa.CHAR(length=11), nullable=True),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('professions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Unicode(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('age_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('consult_time', sa.Unicode(length=64), nullable=True),
    sa.Column('start_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('end_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('try_', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('intro', sa.UnicodeText(), nullable=True),
    sa.Column('closed', sa.Boolean(), nullable=True),
    sa.Column('page_view', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.Integer(), nullable=True),
    sa.Column('cellphone', sa.CHAR(length=11), nullable=True),
    sa.Column('name', sa.Unicode(length=8), nullable=True),
    sa.Column('need', sa.Unicode(length=64), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization', sa.Integer(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'users', sa.Column('identity', sa.CHAR(length=44), nullable=True))
    op.add_column(u'users', sa.Column('last_login', sa.TIMESTAMP(), nullable=True))
    op.add_column(u'users', sa.Column('member_since', sa.TIMESTAMP(), nullable=True))
    op.add_column(u'users', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column(u'users', 'username')
    op.drop_column(u'users', 'member_since')
    op.drop_column(u'users', 'last_login')
    op.drop_column(u'users', 'identity')
    op.drop_table('organization_comments')
    op.drop_table('registers')
    op.drop_table('classes')
    op.drop_table('professions')
    op.drop_table('activity_comments')
    op.drop_table('site_comments')
    op.drop_table('activities')
    op.drop_table('sizes')
    op.drop_table('class_orders')
    op.drop_table('types')
    op.drop_table('ages')
    op.drop_table('organizations')
    op.drop_table('activity_orders')
    op.drop_table('locations')
    op.drop_table('properties')
    op.drop_table('classes_comments')
    op.drop_table('class_time')
    op.drop_table('times')
    ### end Alembic commands ###
