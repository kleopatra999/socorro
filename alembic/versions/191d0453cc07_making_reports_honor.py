"""Making reports honor product and version.

Revision ID: 191d0453cc07
Revises: 523b9e57eba2
Create Date: 2013-10-08 08:00:57.230411

"""

# revision identifiers, used by Alembic.
revision = '191d0453cc07'
down_revision = '523b9e57eba2'

from alembic import op
from socorrolib.lib import citexttype, jsontype
from socorrolib.lib.migrations import load_stored_proc

import sqlalchemy as sa
from sqlalchemy import types
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import table, column




def upgrade():
    op.execute('TRUNCATE signature_summary_device, signature_summary_graphics CASCADE')
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'signature_summary_device', sa.Column(u'version_string', sa.TEXT(), nullable=True))
    op.add_column(u'signature_summary_device', sa.Column(u'product_name', sa.TEXT(), nullable=True))
    op.add_column(u'signature_summary_device', sa.Column(u'product_version_id', sa.INTEGER(), nullable=False))
    op.add_column(u'signature_summary_graphics', sa.Column(u'version_string', sa.TEXT(), nullable=True))
    op.add_column(u'signature_summary_graphics', sa.Column(u'product_name', sa.TEXT(), nullable=True))
    op.add_column(u'signature_summary_graphics', sa.Column(u'product_version_id', sa.INTEGER(), nullable=False))
    op.execute('ALTER TABLE signature_summary_graphics DROP CONSTRAINT signature_summary_graphics_pkey')
    op.execute('ALTER TABLE signature_summary_graphics ADD PRIMARY KEY (report_date, product_version_id, signature_id, graphics_device_id)')
    op.execute('ALTER TABLE signature_summary_device DROP CONSTRAINT signature_summary_device_pkey')
    op.execute('ALTER TABLE signature_summary_device ADD PRIMARY KEY (report_date, product_version_id, signature_id, android_device_id)')
    ### end Alembic commands ###
    load_stored_proc(op, ['update_signature_summary.sql',])

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'signature_summary_graphics', u'product_version_id')
    op.drop_column(u'signature_summary_graphics', u'product_name')
    op.drop_column(u'signature_summary_graphics', u'version_string')
    op.drop_column(u'signature_summary_device', u'product_version_id')
    op.drop_column(u'signature_summary_device', u'product_name')
    op.drop_column(u'signature_summary_device', u'version_string')
    ### end Alembic commands ###
