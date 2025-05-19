$query0 = "
SELECT DISTINCT Code_Delegation, Délégations
FROM population
WHERE Code_Gouvernorat = ?
";

$query1 = "
SELECT Sexe, SUM(Population) AS total_population
FROM population
WHERE Code_Delegation = ?
GROUP BY Sexe
";

$query2 = "
SELECT Sexe, ID_Sexe, SUM(Population) AS total_population
FROM population
WHERE Code_Delegation = ? AND ID_Sexe = ?
GROUP BY Sexe, ID_Sexe
";

$query3 = "
SELECT Sexe, ID_Sexe, Classe_Age, Trancheage, SUM(Population) AS total_population
FROM population
WHERE Code_Delegation = ?
GROUP BY Sexe, ID_Sexe, Trancheage
";

$query4 = "
SELECT Sexe, ID_Sexe, SUM(Population) AS total_population
FROM population
WHERE Code_Delegation= ? AND ID_Sexe = ?
GROUP BY Sexe, ID_Sexe, Trancheage
";

$query5 = "
SELECT Sexe, ID_Sexe, Classe_Age, Trancheage, SUM(Population) AS total_population
FROM population
WHERE Code_Delegation = ? AND ID_Sexe = ?
GROUP BY Sexe, ID_Sexe, Trancheage
";

$query6 = "
SELECT Sexe, SUM(Population) AS total_population
FROM population
WHERE Code_Gouvernorat= ?
GROUP BY Sexe
";

$query7 = "
SELECT Sexe, ID_Sexe, SUM(Population) AS total_population
FROM population
WHERE Code_Gouvernorat = ? AND ID_Sexe = ?
GROUP BY Sexe, ID_Sexe
";

$query8 = "
SELECT Sexe, ID_Sexe, Classe_Age, Trancheage, SUM(Population) AS total_population
FROM population
WHERE Code_Gouvernorat= ?
GROUP BY Sexe, ID_Sexe, Trancheage
";
$query9="
SELECT Sexe, ID_Sexe, SUM(Population) AS total_population
FROM population
WHERE Code_Gouvernorat= ?
GROUP BY Sexe, ID_Sexe, Trancheage
";

$query10="
SELECT Sexe, ID_Sexe,Classe_Age, Trancheage, SUM(Population) AS total_population
FROM population
WHERE Code_Gouvernorat= ? AND ID_Sexe = ?
GROUP BY Sexe, ID_Sexe, Trancheage

";
$query11="
SELECT Sexe, ID_Sexe, SUM(Population) AS total_population
FROM population
WHERE Code_Gouvernorat= ? AND ID_Sexe = ?
GROUP BY Sexe, ID_Sexe, Trancheage";


if (isset($_GET['code_gov'])) {
try {
// Connect to the database

$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);

$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query0);
$stmt->execute([':Code_Gouvernorat' => $_GET['code_gov']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}

}

if (isset($_GET['gouvernorats']) && $_GET['gouvernorats']!=="All" && !isset($_GET['sexe']) && !isset($_GET['age'])) {



$gouvernorat = $_GET['gouvernorats'];

try {
// Connect to the database

$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);

$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare("SELECT DISTINCT Code_Gouvernorat, Gouvernorat FROM population");
$stmt->execute();

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

if (isset($_GET['sexe']) && $_GET['sexe'] == "both" && !isset($_GET['age']) && !isset($_GET['gouvernorats']) &&
isset($_GET['selected_code'])) {
try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query1);
$stmt->execute([':Code_Delegation' => $_GET['selected_code']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe']) && $_GET['sexe'] != "both" && !isset($_GET['age']) && !isset($_GET['gouvernorats']) &&
isset($_GET['selected_code'])) {


try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query2);
$stmt->execute([':Code_Delegation' => $_GET['selected_code'],':ID_Sexe'=>$_GET['sexe']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe']) && isset($_GET['age'])&& $_GET['sexe'] == "both" && $_GET['age'] == "age" &&
!isset($_GET['gouvernorats']) && isset($_GET['selected_code'])) {


try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query3);
$stmt->execute([':Code_Delegation' => $_GET['selected_code']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe'])&& isset($_GET['age']) && $_GET['sexe'] != "both" && $_GET['age'] == "noage" &&
!isset($_GET['gouvernorats']) && isset($_GET['selected_code'])) {


try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query4);
$stmt->execute([':Code_Delegation' => $_GET['selected_code'],':ID_Sexe'=>$_GET['sexe']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}

}

elseif (isset($_GET['sexe'])&& isset($_GET['age']) && $_GET['sexe'] != "both" && $_GET['age'] == "age" &&
!isset($_GET['gouvernorats']) && isset($_GET['selected_code'])) {


try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query5);
$stmt->execute([':Code_Delegation' => $_GET['selected_code'],':ID_Sexe'=>$_GET['sexe']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}


if (isset($_GET['sexe']) && $_GET['sexe'] == "both" && !isset($_GET['age']) && isset($_GET['gouvernorats']) &&
$_GET['gouvernorats']=="1" && isset($_GET['selected_code'])) {

try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query6);
$stmt->execute([':Code_Gouvernorat' => $_GET['selected_code']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe']) && $_GET['sexe'] != "both" && !isset($_GET['age']) && isset($_GET['gouvernorats']) &&
$_GET['gouvernorats']=="1" && isset($_GET['selected_code'])) {

try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query7);
$stmt->execute([':Code_Gouvernorat' => $_GET['selected_code'],':ID_Sexe'=>$_GET['sexe']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe'])&& isset($_GET['age']) && $_GET['sexe'] == "both" && $_GET['age'] == "age" &&
isset($_GET['gouvernorats']) && $_GET['gouvernorats']=="1" && isset($_GET['selected_code'])) {

try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query8);
$stmt->execute([':Code_Gouvernorat' => $_GET['selected_code']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe'])&& isset($_GET['age']) && $_GET['sexe'] == "both" && $_GET['age'] == "noage" &&
isset($_GET['gouvernorats']) && $_GET['gouvernorats']=="1" && isset($_GET['selected_code'])) {
try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query9);
$stmt->execute([':Code_Gouvernorat' => $_GET['selected_code']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe'])&& isset($_GET['age']) && $_GET['sexe'] != "both" && $_GET['age'] == "age" &&
isset($_GET['gouvernorats']) && $_GET['gouvernorats']=="1" && isset($_GET['selected_code'])) {

try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query10);
$stmt->execute([':Code_Gouvernorat' => $_GET['selected_code'],':ID_Sexe'=>$_GET['sexe']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}

elseif (isset($_GET['sexe']) && isset($_GET['age']) && $_GET['sexe'] != "both" && $_GET['age'] == "noage" &&
isset($_GET['gouvernorats']) && $_GET['gouvernorats']=="1" && isset($_GET['selected_code'])) {

try {
// Connect to the database
$pdo = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example query: fetch delegations for a given gouvernorat
$stmt = $pdo->prepare($query11);
$stmt->execute([':Code_Gouvernorat' => $_GET['selected_code'],':ID_Sexe'=>$_GET['sexe']]);

$result = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($result);

} catch (PDOException $e) {
echo json_encode(['error' => $e->getMessage()]);
}
}








if (isset($_GET['gouvernorats']) && $_GET['gouvernorats']=="all" && !isset($_GET['sexe']) && !isset($_GET['age'])) {
   


$gouvernorat = $_GET['gouvernorats'];