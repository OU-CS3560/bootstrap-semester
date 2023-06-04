"""change type of datetime

Revision ID: 166c1446230a
Revises: 27c7c4cb2a5d
Create Date: 2023-06-03 21:29:16.462520

"""
from datetime import date

from alembic import op
import sqlalchemy as sa
from sqlalchemy import select, orm

from app import models

# revision identifiers, used by Alembic.
revision = "166c1446230a"
down_revision = "27c7c4cb2a5d"
branch_labels = None
depends_on = None


"""
class IntermediateClasroom(models.Classroom):
    tmp_begin_date: orm.Mapped[date] = orm.mapped_column(sa.Date())
    tmp_end_date: orm.Mapped[date] = orm.mapped_column(sa.Date())
"""


def upgrade() -> None:
    """
    Note: SQLite does not seem to have support for
    ALTER COLUMN.
    """
    # Upgrade the definition.
    op.add_column("classroom", sa.Column("tmp_begin_date", sa.Date(), nullable=False))
    op.add_column("classroom", sa.Column("tmp_end_date", sa.Date(), nullable=False))

    # Upgrade the data.
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    query = select(models.Classroom)
    results = session.execute(query)
    classrooms = results.scalars().all()
    # Copy data from old column to the new one.
    for c in classrooms:
        c.tmp_begin_date = c.begin_date
        c.tmp_end_date = c.end_date

    # Switch to the new columns.
    op.drop_column("classroom", "begin_date")
    op.drop_column("classroom", "end_date")
    op.alter_column("classroom", "tmp_begin_date", new_column_name="begin_date")
    op.alter_column("classroom", "tmp_end_date", new_column_name="end_date")


def downgrade() -> None:
    pass
