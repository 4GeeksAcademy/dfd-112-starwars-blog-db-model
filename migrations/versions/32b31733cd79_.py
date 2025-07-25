"""empty message

Revision ID: 32b31733cd79
Revises: a5cffa318ac2
Create Date: 2025-07-25 19:06:43.148053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b31733cd79'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('birth_year', sa.String(length=100), nullable=False),
    sa.Column('eye_color', sa.String(length=100), nullable=False),
    sa.Column('gender', sa.String(length=100), nullable=False),
    sa.Column('hair_color', sa.String(length=100), nullable=False),
    sa.Column('height', sa.String(length=20), nullable=False),
    sa.Column('mass', sa.String(length=40), nullable=False),
    sa.Column('skin_color', sa.String(length=20), nullable=False),
    sa.Column('homeworld', sa.String(length=40), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('edited', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('diameter', sa.String(length=100), nullable=False),
    sa.Column('rotation_period', sa.String(length=100), nullable=False),
    sa.Column('orbital_period', sa.String(length=100), nullable=False),
    sa.Column('gravity', sa.String(length=100), nullable=False),
    sa.Column('population', sa.String(length=100), nullable=False),
    sa.Column('climate', sa.String(length=100), nullable=False),
    sa.Column('terrain', sa.String(length=100), nullable=False),
    sa.Column('surface_water', sa.String(length=100), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('edited', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('vehicle_class', sa.String(length=100), nullable=False),
    sa.Column('manufacturer', sa.String(length=100), nullable=False),
    sa.Column('length', sa.String(length=100), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=100), nullable=False),
    sa.Column('crew', sa.String(length=20), nullable=False),
    sa.Column('passengers', sa.String(length=20), nullable=False),
    sa.Column('max_atmos_speed', sa.String(length=100), nullable=False),
    sa.Column('cargo_capacity', sa.String(length=100), nullable=False),
    sa.Column('consumables', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('edited', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=40), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=60), nullable=False))
        batch_op.add_column(sa.Column('creation', sa.DateTime(timezone=True), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=40),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=40),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=40),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('creation')
        batch_op.drop_column('name')
        batch_op.drop_column('username')

    op.drop_table('favorite')
    op.drop_table('vehicle')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
