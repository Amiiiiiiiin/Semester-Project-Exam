"""Full text search columns + indexes

Revision ID: 852baab5b87e
Revises: dc63297d8382
Create Date: 2023-12-13 19:04:31.116781

"""
import sqlalchemy as sa
from alembic import op
from rpg_api.db.postgres.base import TSVector

# revision identifiers, used by Alembic.
revision = "852baab5b87e"
down_revision = "dc63297d8382"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "ability", sa.Column("description", sa.String(length=500), nullable=True)
    )
    op.add_column(
        "ability",
        sa.Column(
            "ts_vector",
            TSVector(),
            sa.Computed(
                "to_tsvector('english', name || ' ' || description)", persisted=True
            ),
            nullable=True,
        ),
    )
    op.drop_index("idx_ability_name", table_name="ability")
    op.create_index(
        "idx_ability_name_description_ts_vector",
        "ability",
        ["ts_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.add_column(
        "ability_type",
        sa.Column(
            "ts_vector",
            TSVector(),
            sa.Computed(
                "to_tsvector('english', name || ' ' || description)", persisted=True
            ),
            nullable=True,
        ),
    )
    op.alter_column(
        "ability_type",
        "description",
        existing_type=sa.VARCHAR(length=500),
        nullable=True,
    )
    op.drop_index("idx_ability_type_name", table_name="ability_type")
    op.create_index(
        "idx_ability_type_name_description_ts_vector",
        "ability_type",
        ["ts_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.add_column(
        "attribute",
        sa.Column(
            "ts_vector",
            TSVector(),
            sa.Computed(
                "to_tsvector('english', name || ' ' || description)", persisted=True
            ),
            nullable=True,
        ),
    )
    op.alter_column(
        "attribute", "description", existing_type=sa.VARCHAR(length=500), nullable=True
    )
    op.drop_index("idx_attribute_name", table_name="attribute")
    op.create_index(
        "idx_attribute_name_name_description_ts_vector",
        "attribute",
        ["ts_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.add_column(
        "base_class", sa.Column("description", sa.String(length=500), nullable=True)
    )
    op.add_column(
        "base_class",
        sa.Column(
            "ts_vector",
            TSVector(),
            sa.Computed(
                "to_tsvector('english', name || ' ' || description)", persisted=True
            ),
            nullable=True,
        ),
    )
    op.drop_index("idx_base_class_name", table_name="base_class")
    op.create_index(
        "idx_base_class_name_description_ts_vector",
        "base_class",
        ["ts_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.add_column(
        "place", sa.Column("description", sa.String(length=500), nullable=True)
    )
    op.add_column(
        "place",
        sa.Column(
            "ts_vector",
            TSVector(),
            sa.Computed(
                "to_tsvector('english', name || ' ' || description)", persisted=True
            ),
            nullable=True,
        ),
    )
    op.drop_index("idx_place_name", table_name="place")
    op.create_index(
        "idx_place_name_description_ts_vector",
        "place",
        ["ts_vector"],
        unique=False,
        postgresql_using="gin",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "idx_place_name_description_ts_vector",
        table_name="place",
        postgresql_using="gin",
    )
    op.create_index("idx_place_name", "place", ["name"], unique=False)
    op.drop_column("place", "ts_vector")
    op.drop_column("place", "description")
    op.drop_index(
        "idx_base_class_name_description_ts_vector",
        table_name="base_class",
        postgresql_using="gin",
    )
    op.create_index("idx_base_class_name", "base_class", ["name"], unique=False)
    op.drop_column("base_class", "ts_vector")
    op.drop_column("base_class", "description")
    op.drop_index(
        "idx_attribute_name_name_description_ts_vector",
        table_name="attribute",
        postgresql_using="gin",
    )
    op.create_index("idx_attribute_name", "attribute", ["name"], unique=False)
    op.alter_column(
        "attribute", "description", existing_type=sa.VARCHAR(length=500), nullable=False
    )
    op.drop_column("attribute", "ts_vector")
    op.drop_index(
        "idx_ability_type_name_description_ts_vector",
        table_name="ability_type",
        postgresql_using="gin",
    )
    op.create_index("idx_ability_type_name", "ability_type", ["name"], unique=False)
    op.alter_column(
        "ability_type",
        "description",
        existing_type=sa.VARCHAR(length=500),
        nullable=False,
    )
    op.drop_column("ability_type", "ts_vector")
    op.drop_index(
        "idx_ability_name_description_ts_vector",
        table_name="ability",
        postgresql_using="gin",
    )
    op.create_index("idx_ability_name", "ability", ["name"], unique=False)
    op.drop_column("ability", "ts_vector")
    op.drop_column("ability", "description")
    # ### end Alembic commands ###