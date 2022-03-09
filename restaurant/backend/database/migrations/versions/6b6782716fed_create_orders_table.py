from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6b6782716fed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('costumer_id', sa.Integer, nullable=False),
        sa.Column('status', sa.String(25), nullable=False),
        sa.Column('total_price', sa.Float, nullable=False),
    )


def downgrade():
    op.drop_table('orders')
