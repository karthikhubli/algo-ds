'''
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like:
"Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given an integer n and a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

Note that the n x n 2D array graph given as input is not directly available to you, and instead only accessible through
the helper function knows. graph[i][j] == 1 represents person i knows person j, wherease graph[i][j] == 0 represents person j does not know person i.

Example 1:


Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise
graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

'''


# Function to find the celebrity
def celebrity(mat):
    n = len(mat)
    st = []

    # Push everybody in stack
    for i in range(n):
        st.append(i)

    # Find a potential celebrity
    while len(st) > 1:

        a = st.pop()
        b = st.pop()

        # if a knows b
        knows = mat[a][b]
        if knows:
            st.append(b)
        else:
            st.append(a)

    # Potential candidate of celebrity
    c = st.pop()

    # Check if c is actually
    # a celebrity or not
    for i in range(n):
        if i == c:
            continue

        # If any person doesn't
        # know 'c' or 'c' doesn't
        # know any person, return -1
        if mat[c][i] or not mat[i][c]:
            return -1

    return c

def celeb_map(mat):
    in_map = dict()
    out_map = dict()
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                if i in out_map.keys():
                    out_map[i] +=1
                else:
                    out_map[i] = 1
                if j in in_map.keys():
                    in_map[j] +=1
                else:
                    in_map[j] = 1

    print(in_map)
    print(out_map)
    for k,v in out_map.items():
        if v == 1:
            if in_map[k] == n:
                return k
            else:
                return -1
    return -1

def test_celeb(mat):
    n = len(mat)
    canditate = []
    for i in range(n):
        if mat[i].count(1) == 1:
            canditate.append(i)
    if len(canditate) == 1:
        c = canditate[0]
        for j in range(n):
            if j != i:
                if mat[c][j] != 0:
                    return -1
            return c
    return -1




if __name__ == "__main__":
    mat = [[1,1,0,1],
           [0,1,0,0],
           [1,1,1,1],
           [0,1,0,1]]
    # mat = [[1,1,0],[0,1,0],[1,1,1]]
    print(celeb_map(mat))