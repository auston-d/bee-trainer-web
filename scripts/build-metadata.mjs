import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
export function buildMetadata(root) {
  const git = (...args) => { try { return execFileSync('git', args, { cwd: root, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim(); } catch { return null; } };
  const { version } = JSON.parse(readFileSync(new URL('../release.json', import.meta.url), 'utf8'));
  const environment = process.env.BEE_DEPLOY_ENV || 'local';
  if (!['development', 'production', 'local'].includes(environment)) throw new Error('Invalid BEE_DEPLOY_ENV');
  const commit = process.env.BEE_COMMIT_SHA || git('rev-parse', 'HEAD');
  if (environment !== 'local' && !/^[a-f0-9]{40}$/.test(commit || '')) throw new Error('Deployment requires the exact source commit SHA');
  return { version, commit, branch: process.env.BEE_DEPLOY_BRANCH || git('branch', '--show-current') || null, environment, builtAt: new Date().toISOString() };
}
