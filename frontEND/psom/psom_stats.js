// src/PlayerStats.js
import React, { useEffect, useState } from 'react';

function PlayerStats() {
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/players')  // Adjust the URL if needed
      .then((response) => response.json())
      .then((data) => {
        setPlayers(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>Basketball Player Stats</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Points</th>
            <th>Assists</th>
            <th>Rebounds</th>
          </tr>
        </thead>
        <tbody>
          {players.map((player) => (
            <tr key={player.name}>
              <td>{player.name}</td>
              <td>{player.points}</td>
              <td>{player.assists}</td>
              <td>{player.rebounds}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default PlayerStats;
