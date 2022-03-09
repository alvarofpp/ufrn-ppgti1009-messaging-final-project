from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '384f7d6083f5'
down_revision = '6b6782716fed'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('order_id', sa.Integer, nullable=False),
    )
    op.create_foreign_key(
        constraint_name='fk_orders_id',
        source_table='items',
        local_cols=['order_id'],
        referent_table='orders',
        remote_cols=['id'],
    )


def downgrade():
    op.drop_table('items')
