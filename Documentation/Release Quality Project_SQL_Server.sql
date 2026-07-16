CREATE TABLE [Projects] (
  [project_id] integer PRIMARY KEY IDENTITY(1, 1),
  [project_name] text NOT NULL,
  [owner] text,
  [status] text NOT NULL
)
GO

CREATE TABLE [Releases] (
  [release_id] integer PRIMARY KEY IDENTITY(1, 1),
  [project_id] integer NOT NULL,
  [release_name] text NOT NULL,
  [environment] text NOT NULL,
  [planned_date] text,
  [actual_date] text,
  [status] text NOT NULL
)
GO

CREATE TABLE [Users] (
  [user_id] integer PRIMARY KEY IDENTITY(1, 1),
  [full_name] text NOT NULL,
  [role] text NOT NULL
)
GO

CREATE TABLE [Bugs] (
  [bug_id] integer PRIMARY KEY IDENTITY(1, 1),
  [release_id] integer NOT NULL,
  [reporter_id] integer NOT NULL,
  [assignee_id] integer NOT NULL,
  [title] text NOT NULL,
  [description] text,
  [priority] text NOT NULL,
  [severity] text NOT NULL,
  [status] text NOT NULL,
  [created_date] text NOT NULL,
  [closed_date] text
)
GO

CREATE TABLE [TestCases] (
  [testcase_id] integer PRIMARY KEY IDENTITY(1, 1),
  [release_id] integer NOT NULL,
  [executed_by] integer NOT NULL,
  [title] text NOT NULL,
  [test_type] text NOT NULL,
  [priority] text NOT NULL,
  [status] text NOT NULL,
  [execution_date] text NOT NULL
)
GO

ALTER TABLE [Releases] ADD FOREIGN KEY ([project_id]) REFERENCES [Projects] ([project_id])
GO

ALTER TABLE [Bugs] ADD FOREIGN KEY ([release_id]) REFERENCES [Releases] ([release_id])
GO

ALTER TABLE [Bugs] ADD FOREIGN KEY ([reporter_id]) REFERENCES [Users] ([user_id])
GO

ALTER TABLE [Bugs] ADD FOREIGN KEY ([assignee_id]) REFERENCES [Users] ([user_id])
GO

ALTER TABLE [TestCases] ADD FOREIGN KEY ([release_id]) REFERENCES [Releases] ([release_id])
GO

ALTER TABLE [TestCases] ADD FOREIGN KEY ([executed_by]) REFERENCES [Users] ([user_id])
GO
