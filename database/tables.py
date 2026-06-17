
CREATE_AGENTS_TABLE = """
    CREATE TABLE IF NOT EXISTS agents(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    specialty VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    completed_missions INT NOT NULL DEFAULT 0,
    failed_missions  INT NOT NULL DEFAULT 0,
    agent_rank ENUM('Junior', 'Senior', 'Commander')
    )
"""

CREATE_MISSIONS_TABLE = """
    CREATE TABLE IF NOT EXISTS missions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    description TEXT, 
    location VARCHAR(250) NOT NULL,
    difficulty INT NOT NULL,
    importance INT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'NEW',
    risk_level VARCHAR(50) NOT NULL, 
    assigned_agent_id INT DEFAULT NULL,
    FOREIGN KEY (assigned_agent_id) REFERENCES agents(id) ON DELETE SET NULL
    )
"""