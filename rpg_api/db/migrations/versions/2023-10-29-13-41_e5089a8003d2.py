"""empty message

Revision ID: e5089a8003d2
Revises: 81ad9ce9c20d
Create Date: 2023-10-29 13:41:48.998109

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e5089a8003d2"
down_revision = "81ad9ce9c20d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "base_character",
        sa.Column("base_class_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column(
            "gender", sa.Enum("male", "female", "other", name="gender"), nullable=False
        ),
        sa.Column("character_name", sa.String(length=50), nullable=False),
        sa.Column("alive", sa.Boolean(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("xp", sa.Integer(), nullable=False),
        sa.Column("money", sa.Integer(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["base_class_id"],
            ["base_class.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["base_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "character_location",
        sa.Column("base_character_id", sa.UUID(), nullable=False),
        sa.Column("x", sa.Integer(), nullable=False),
        sa.Column("y", sa.Integer(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["base_character_id"],
            ["base_character.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("character_location")
    op.drop_table("base_character")
    # ### end Alembic commands ###
