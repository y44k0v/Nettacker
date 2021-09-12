#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

elastic_search_types = {
    "ScanEvents": {
        'mappings': {
            'properties': {
                'target': {'type': 'keyword'},
                'module_name': {'type': 'keyword'},
                'machine_name': {'type': 'keyword'},
                'scan_unique_id': {'type': 'keyword'},
                'event': {'type': 'nested'},
                'date': {
                    'type': 'date',
                    'format': 'yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis'
                }
            }
        }
    },
    "TemporaryScanEvents": {
        'mappings': {
            'properties': {
                'target': {'type': 'keyword'},
                'module_name': {'type': 'keyword'},
                'machine_name': {'type': 'keyword'},
                'scan_unique_id': {'type': 'keyword'},
                'event_name': {'type': 'keyword'},
                'event': {'type': 'nested'},
                'date': {
                    'type': 'date',
                    'format': 'yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis'
                }
            }
        }
    },
    "Scans": {
        'mappings': {
            'properties': {
                'scan_unique_id': {'type': 'keyword'},
                'status': {'type': 'keyword'},
                'report_path_filename': {'type': 'text'},
                'md5': {'type': 'keyword'},
                'file_content': {'type': 'binary'},
                'date': {
                    'type': 'date',
                    'format': 'yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis'
                },
                'finished_date': {
                    'type': 'date',
                    'format': 'yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis'
                }
            }
        }
    }
}
