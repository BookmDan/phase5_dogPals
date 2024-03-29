"""init migrate

Revision ID: 71cf20c17438
Revises: 
Create Date: 2024-03-03 16:24:21.147308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71cf20c17438'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email'))
    )
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('breed', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name=op.f('fk_dogs_owner_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_dogs'))
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], name=op.f('fk_messages_receiver_id_users')),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], name=op.f('fk_messages_sender_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_messages'))
    )
    op.create_table('sitters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('availability', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_sitters_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_sitters'))
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sitter_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['sitter_id'], ['sitters.id'], name=op.f('fk_reviews_sitter_id_sitters')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviews_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('sitter_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.DECIMAL(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['sitter_id'], ['sitters.id'], name=op.f('fk_transactions_sitter_id_sitters')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_transactions_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_transactions'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('reviews')
    op.drop_table('sitters')
    op.drop_table('messages')
    op.drop_table('dogs')
    op.drop_table('users')
    # ### end Alembic commands ###
