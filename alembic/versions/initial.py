from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('groups',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('students',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('fullname', sa.String(), nullable=False),
                    sa.Column('group_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('teachers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('fullname', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('subjects',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('teacher_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('grades',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('student_id', sa.Integer(), nullable=False),
                    sa.Column('subject_id', sa.Integer(), nullable=False),
                    sa.Column('grade', sa.Integer(), nullable=False),
                    sa.Column('grade_date', sa.Date(), nullable=False),
                    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
                    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('grades')
    op.drop_table('subjects')
    op.drop_table('teachers')
    op.drop_table('students')
    op.drop_table('groups')
