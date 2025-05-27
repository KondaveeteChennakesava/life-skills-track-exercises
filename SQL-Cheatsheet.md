
# Databases

## 📚 Introduction

Databases are at the core of nearly every modern software system. To ensure reliability, performance, and data integrity, it’s important to understand the fundamental concepts that underpin how databases operate. This paper explores essential database topics: **ACID**, **CAP Theorem**, **Joins**, **Aggregations**, **Filters**, **Normalization**, **Indexes**, **Transactions**, **Locking Mechanisms**, **Isolation Levels**, and **Triggers**.

---

## ACID Properties

ACID is a set of properties that guarantee database transactions are processed reliably.

1. **Atomicity**: Ensures that a transaction is all or nothing. If one part fails, the entire transaction is rolled back.
2. **Consistency**: Guarantees that a transaction brings the database from one valid state to another, maintaining data integrity.
3. **Isolation**: Ensures that concurrent execution of transactions leaves the database in the same state as if the transactions were executed sequentially.
4. **Durability**: Once a transaction is committed, the changes are permanent—even in the event of a system failure.

---

## CAP Theorem

Proposed by Eric Brewer, CAP theorem states that a distributed database can provide only two of the following three guarantees simultaneously:

- **Consistency**: Every read receives the most recent write.
- **Availability**: Every request gets a response, without guarantee that it contains the most recent version of the information.
- **Partition Tolerance**: The system continues to operate despite arbitrary message loss or failure of part of the system.

| Combination         | Description                                |
|---------------------|--------------------------------------------|
| CP (e.g., HBase)     | Consistent and Partition-tolerant         |
| CA (theoretical)     | Consistent and Available (no partition tolerance) |
| AP (e.g., CouchDB)   | Available and Partition-tolerant          |

---

## Joins in SQL

Joins allow data to be combined from two or more tables based on a related column.

- **INNER JOIN**: Returns only the rows with matching values in both tables.
- **LEFT JOIN**: Returns all rows from the left table and matched rows from the right.
- **RIGHT JOIN**: Returns all rows from the right table and matched rows from the left.
- **FULL OUTER JOIN**: Returns all rows when there is a match in one of the tables.

```sql
SELECT employees.name, departments.name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.id;
```

---

## Aggregations & Filters

- **Aggregations**: Used to perform calculations on multiple rows (e.g., `SUM`, `COUNT`, `AVG`, `MAX`, `MIN`).

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```

- **Filters**: Used to retrieve specific data using `WHERE`, `HAVING`, and logical operators.

```sql
SELECT * FROM orders
WHERE amount > 500 AND status = 'Completed';
```

---

## Normalization

Normalization is the process of structuring a relational database to reduce redundancy and improve data integrity.

- **1NF**: Eliminate repeating groups; ensure atomicity.
- **2NF**: Remove partial dependencies (non-prime attributes fully depend on the primary key).
- **3NF**: Remove transitive dependencies.
- **BCNF**: Every determinant is a candidate key.

Benefits:
- Avoids data anomalies
- Makes data more maintainable

---

## Indexes

Indexes improve the speed of data retrieval but can slow down write operations.

- **Types**:
  - **Single-column index**
  - **Composite index** (multiple columns)
  - **Unique index**
  - **Full-text index**
  - **Hash/B-tree index** (depending on DB engine)

```sql
CREATE INDEX idx_name ON employees(last_name);
```

Trade-offs:
- Faster SELECTs
- Slower INSERTs/UPDATEs
- Additional storage cost

---

## Transactions

A **transaction** is a unit of work performed within a database management system.

### Lifecycle of a transaction:
1. **Begin Transaction**
2. **Perform operations**
3. **Commit** (make permanent) or **Rollback** (undo)

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

---

## Locking Mechanism

Locks prevent concurrent transactions from interfering with each other.

- **Types of Locks**:
  - **Shared Lock (S)**: Read-only, can be held by multiple transactions.
  - **Exclusive Lock (X)**: Write, only one transaction can hold.

- **Granularity**:
  - Row-level
  - Page-level
  - Table-level

**Deadlocks** occur when transactions wait on each other’s locks indefinitely.

---

## Database Isolation Levels

Isolation level determines the visibility of data between transactions.

| Level            | Dirty Read | Non-repeatable Read | Phantom Read |
|------------------|------------|----------------------|--------------|
| Read Uncommitted | ✅          | ✅                    | ✅            |
| Read Committed   | ❌          | ✅                    | ✅            |
| Repeatable Read  | ❌          | ❌                    | ✅            |
| Serializable     | ❌          | ❌                    | ❌            |

- **Dirty Read**: Reading uncommitted data
- **Non-repeatable Read**: Re-reading the same row yields different data
- **Phantom Read**: New rows appear when a range is queried again

---

## Triggers

A **trigger** is a set of SQL statements that automatically executes when a specific event occurs on a table.

### Types of triggers:
- **BEFORE INSERT/UPDATE/DELETE**
- **AFTER INSERT/UPDATE/DELETE**

```sql
CREATE TRIGGER log_salary_change
AFTER UPDATE ON employees
FOR EACH ROW
WHEN (OLD.salary <> NEW.salary)
BEGIN
  INSERT INTO salary_logs(emp_id, old_salary, new_salary)
  VALUES (OLD.id, OLD.salary, NEW.salary);
END;
```

---

## Conclusion

Understanding these core database concepts helps engineers build more robust, efficient, and scalable systems. From enforcing data integrity with **ACID** to optimizing performance with **indexes** and **normalization**, and ensuring safe concurrent access with **transactions and locks**, these foundational principles are essential to every software developer's toolkit.

---
