"""Initial Migration

Revision ID: 976facb08797
Revises: a8e9998c1818
Create Date: 2021-08-15 19:25:02.974044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '976facb08797'
down_revision = 'a8e9998c1818'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(length=120), nullable=False))
    op.add_column('users', sa.Column('about', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('avatar', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password_encrypt', sa.String(length=128), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password_encrypt')
    op.drop_column('users', 'avatar')
    op.drop_column('users', 'about')
    op.drop_column('users', 'email')
    op.drop_column('pitches', 'category')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitch_id')
    op.drop_table('likes')
    # ### end Alembic commands ###
