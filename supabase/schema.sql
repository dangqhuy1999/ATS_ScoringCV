-- Upload this via Supabase SQL Editor
CREATE TABLE candidates (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT,
  cv_text TEXT,
  score FLOAT,
  job_id INTEGER,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE jobs (
  id SERIAL PRIMARY KEY,
  title TEXT,
  jd TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Enable file uploads (Supabase Storage)
-- Bucket: "cv-files"

