from datetime import datetime
from typing import List, Optional

from sqlalchemy import Integer, String, Table, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(256))


class Classroom(Base):
    __tablename__ = "classroom"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    begin_date: Mapped[datetime] = mapped_column(DateTime())
    end_date: Mapped[datetime] = mapped_column(DateTime())
    github_classroom_link: Mapped[Optional[str]] = mapped_column(String(2048))

    students: Mapped[list["Student"]] = relationship()
    milestones: Mapped[list["Milestone"]] = relationship()
    teams: Mapped[list["Team"]] = relationship()


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(256))
    last_name: Mapped[str] = mapped_column(String(256))
    username: Mapped[str] = mapped_column(String(256))
    github_username: Mapped[Optional[str]] = mapped_column(String(256))
    is_drop: Mapped[bool] = mapped_column(Boolean(), default=False)
    note: Mapped[str] = mapped_column(Text(), default="")

    classroom_id: Mapped[int] = mapped_column(ForeignKey("classroom.id"))
    classroom: Mapped["Classroom"] = relationship(back_populates="students")

    team_id: Mapped[Optional[int]] = mapped_column(ForeignKey("team.id"))
    team: Mapped[Optional["Team"]] = relationship(back_populates="members")


class Milestone(Base):
    __tablename__ = "milestone"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    begin_date: Mapped[datetime] = mapped_column(DateTime())
    end_date: Mapped[datetime] = mapped_column(DateTime())

    classroom_id: Mapped[int] = mapped_column(ForeignKey("classroom.id"))
    classroom: Mapped["Classroom"] = relationship(back_populates="milestones")

    presentations: Mapped[list["Presentation"]] = relationship()


class StudentPresentationAssociation(Base):
    __tablename__ = "student_presentation_association"
    presentation_id: Mapped[int] = mapped_column(
        ForeignKey("presentation.id"), primary_key=True
    )
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"), primary_key=True)
    is_presented: Mapped[bool] = mapped_column(Boolean())
    note: Mapped[str] = mapped_column(Text())

    student: Mapped["Student"] = relationship()


class Presentation(Base):
    __tablename__ = "presentation"
    id: Mapped[int] = mapped_column(primary_key=True)
    team_note: Mapped[str] = mapped_column(Text())

    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    team: Mapped["Team"] = relationship(back_populates="presentations")

    milestone_id: Mapped[int] = mapped_column(ForeignKey("milestone.id"))
    milestone: Mapped["Milestone"] = relationship(back_populates="presentations")

    speakers: Mapped[List["StudentPresentationAssociation"]] = relationship()


class Team(Base):
    __tablename__ = "team"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    project_brief: Mapped[str] = mapped_column(Text())
    technology_platform_description: Mapped[str] = mapped_column(Text())

    classroom_id: Mapped[int] = mapped_column(ForeignKey("classroom.id"))
    classroom: Mapped["Classroom"] = relationship(back_populates="teams")

    members: Mapped[list["Student"]] = relationship()
    presentations: Mapped[list["Presentation"]] = relationship()
