# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''



    query= """SELECT O.OrderID, C.ContactName, E.FirstName
    FROM Orders O
    JOIN Customers C ON O.CustomerID = C.CustomerID
    JOIN Employees E  ON O.EmployeeID = E.EmployeeID
    ORDER BY O.OrderID """

    db.execute(query)
    results = db.fetchall()

    return  results



def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query= """SELECT
    Customers.ContactName,
    SUM(details.UnitPrice * details.Quantity) AS cumulative_amount
    FROM OrderDetails AS details
    JOIN Orders ON details.OrderID = Orders.OrderId
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    GROUP BY ContactName
    ORDER BY cumulative_amount """

    db.execute(query)
    results = db.fetchall()

    return results







def best_employee(db):
    """Implement the best_employee method to determine who's the best employee!
    By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like:
    ('FirstName', 'LastName', 6000 (the sum of all purchase)).
    The order of the information is irrelevant"""
    query = """
    SELECT E.FirstName, E.LastName, SUM(od.Quantity * od.UnitPrice) AS TotalSales
    FROM Orders O
    JOIN Employees E ON O.EmployeeID = E.EmployeeID
    JOIN OrderDetails od ON O.OrderID = od.OrderID
    GROUP BY E.EmployeeID
    ORDER BY TotalSales DESC
    LIMIT 1
    """
    db.execute(query)
    results = db.fetchone()
    return results
def orders_per_customer(db):
    """Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders"""
    query = """
    SELECT C.ContactName, COUNT(O.OrderID) AS NumberOfOrders
    FROM Customers C
    LEFT JOIN Orders O ON C.CustomerID = O.CustomerID
    GROUP BY C.ContactName
    ORDER BY NumberOfOrders ASC
    """
    db.execute(query)
    results = db.fetchall()
    return results
