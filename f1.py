import sys

if args.match_host and not any([local_peer == args.match_host, remote_peer == args.match_host]):
                # If a match_host is given but neither local_peer nor remote_peer match
                continue

            if first_switched not in pending:
                pending[first_switched] = {}

            # Match peers
            if remote_peer in pending[first_switched]:
                # The destination peer put itself into the pending dict, getting and removing entry
                peer_flow = pending[first_switched].pop(remote_peer)
                if len(pending[first_switched]) == 0: